import json
def aggregate_data(input_data):
    circuit1_data = input_data.get('circuit1', {}).copy()
    circuit2_data = input_data.get('circuit2', {}).copy()

    for key in sorted(input_data.keys()):
        if not key.startswith("circuit"):
            continue

        circuit_num = int(key.split("circuit")[1])
        if circuit_num in [1, 2]:
            continue

        target_data = circuit1_data if circuit_num % 2 == 1 else circuit2_data

        for k, v in input_data[key].items():
            if k in target_data:
                if isinstance(target_data[k], list):
                    for item in (v if isinstance(v, list) else [v]):
                        if item not in target_data[k]:
                            target_data[k].append(item)
                else:
                    existing = [target_data[k]]
                    additional = v if isinstance(v, list) else [v]
                    target_data[k] = existing + [i for i in additional if i not in existing]
            else:
                target_data[k] = v

    return circuit1_data, circuit2_data

    
def sort_based_on_reference(source, reference):
    source_list = list(source)
    reference_list = list(reference)
    sorted_source = sorted(source_list, key=lambda x: reference_list.index(x) if x in reference_list else float('inf'))
    extra_keys = [k for k in reference_list if k not in source_list]
    sorted_source.extend(extra_keys)
    return sorted_source
def process(input_data):
    circuit1_data = input_data['circuit1']
    circuit2_data = input_data['circuit2']

    circuit1_sorted_keys = sort_based_on_reference(circuit1_data, circuit2_data)
    result = {}

    pin_unique_counter = 0

    for pin_name in circuit1_sorted_keys:
        pin_data_c1 = circuit1_data.get(pin_name, [])
        pin_data_c2 = circuit2_data.get(pin_name, [])

        nets = {}
        net_unique_counter = 0
        all_nets = set([entry[0] for entry in pin_data_c1 if isinstance(entry, list)]) | set([entry[0] for entry in pin_data_c2 if isinstance(entry, list)])
        
        for net in sorted(all_nets):  # Using sorted to ensure a deterministic order
            net_entry_c1 = next((item for item in pin_data_c1 if isinstance(item, list) and item[0] == net), None)
            net_entry_c2 = next((item for item in pin_data_c2 if isinstance(item, list) and item[0] == net), None)

            net_in_c1 = net_entry_c1[0] if net_entry_c1 else "0"
            net_in_c2 = net_entry_c2[0] if net_entry_c2 else "0"

            # Decide the key for the nets dictionary based on whether pin is in circuit2 or not
            if pin_data_c2:
                key = net_in_c2
            else:
                key = str(net_unique_counter)
                net_unique_counter += 1

            nets[key] = [net_in_c2, net_in_c1]

        if pin_data_c1 and pin_data_c2:
            result[pin_name] = [f"{pin_name}({pin_data_c2[-1]})", f"{pin_name}({pin_data_c1[-1]})", nets]
        else:
            if len(pin_data_c1) == 1 and isinstance(pin_data_c1[0], list):
                result[pin_name] = [pin_name, f"{pin_data_c1[0][1]}({pin_data_c1[0][2]})", nets]
            elif pin_data_c1:
                unique_key = str(pin_unique_counter)
                pin_name_value_c1 = pin_data_c1[-1] if pin_data_c1 else "0"
                
                result[unique_key] = ["0", f"{pin_name}({pin_name_value_c1})", nets]
                pin_unique_counter += 1  # Increment by 1 for each unique pin key
            elif pin_data_c2:
                result[pin_name] = [f"{pin_name}({pin_data_c2[-1]})", "0", nets]

    return result



def generate_json_output(processed_data):
    output = {"pins": processed_data}

    with open("output_pins.json", "w") as outfile:
        json.dump(output, outfile, indent=4)


if __name__ == "__main__":
    data =   {'circuit1': {'K': [['sky130_fd_pr__nfet_01v8', 'drain|source', 1], ['sky130_fd_pr__pfet_01v8_hvt', 'drain|source', 1], 3], 'L': [['sky130_fd_pr__nfet_01v8', 'gate', 1], ['sky130_fd_pr__pfet_01v8_hvt', 'gate', 1], 3]}, 'circuit2': {'R': [['sky130_fd_pr__nfet_01v8', '2', 1], ['sky130_fd_pr__pfet_01v8_hvt', '2', 1], 3], 'Y': [['sky130_fd_pr__nfet_01v8', '1|3', 1], ['sky130_fd_pr__pfet_01v8_hvt', '1|3', 1], 3]}, 'circuit3': {'dummy_14': [['sky130_fd_pr__pfet_01v8_hvt', 'proxy4', 1], 0], 'dummy_13': [['sky130_fd_pr__pfet_01v8_hvt', 'proxy3', 1], 0], 'dummy_12': [['sky130_fd_pr__pfet_01v8_hvt', 'proxy2', 1], 0], 'dummy_11': [['sky130_fd_pr__pfet_01v8_hvt', 'proxy1', 1], 0], 'dummy_10': [['sky130_fd_pr__nfet_01v8', 'proxy4', 1], 0], 'dummy_9': [['sky130_fd_pr__nfet_01v8', 'proxy3', 1], 0], 'dummy_8': [['sky130_fd_pr__nfet_01v8', 'proxy2', 1], 0], 'dummy_7': [['sky130_fd_pr__nfet_01v8', 'proxy1', 1], 0], 'VPB': [['sky130_fd_pr__pfet_01v8_hvt', 'bulk', 1], 2], 'VPWR': [['sky130_fd_pr__pfet_01v8_hvt', 'drain|source', 1], 2], 'VNB': [['sky130_fd_pr__nfet_01v8', 'bulk', 1], 2], 'VGND': [['sky130_fd_pr__nfet_01v8', 'drain|source', 1], 2]}, 'circuit4': {'Dum': [['sky130_fd_pr__pfet_01v8_hvt', 'proxybulk', 1], 0], 'dummy_13': [['sky130_fd_pr__pfet_01v8_hvt', 'proxysource', 1], 0], 'dummy_12': [['sky130_fd_pr__pfet_01v8_hvt', 'proxygate', 1], 0], 'dummy_11': [['sky130_fd_pr__pfet_01v8_hvt', 'proxydrain', 1], 0], 'dummy_10': [['sky130_fd_pr__nfet_01v8', 'proxybulk', 1], 0], 'dummy_9': [['sky130_fd_pr__nfet_01v8', 'proxysource', 1], 0], 'dummy_8': [['sky130_fd_pr__nfet_01v8', 'proxygate', 1], 0], 'dummy_7': [['sky130_fd_pr__nfet_01v8', 'proxydrain', 1], 0], 'VPB': [['sky130_fd_pr__pfet_01v8_hvt', '4', 1], 2], 'VPWR': [['sky130_fd_pr__pfet_01v8_hvt', '1|3', 1], 2], 'VNB': [['sky130_fd_pr__nfet_01v8', '4', 1], 2], 'VGND': [['sky130_fd_pr__nfet_01v8', '1|3', 1], 2]}}
    circuit1_data, circuit2_data = aggregate_data(data)
    data = {'circuit1': circuit1_data, 'circuit2': circuit2_data}  # Overwrite original data for processing
    processed_data = process(data)
    generate_json_output(processed_data)
