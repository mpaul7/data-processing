
#!/bin/bash
# Executed


#Pending 

# Execute scp commands one by one
for cmd in \
"scp solana@192.168.10.211:/data/Solana_datasets/js-data/data/2020a_Wireline_Ethernet/data_beta.orc 2020a_Wireline_Ethernet" \
"scp solana@192.168.10.211:/data/Solana_datasets/js-data/data/2020c_Mobile_Wifi/data_beta.orc 2020c_Mobile_Wifi" \
"scp solana@192.168.10.211:/data/Solana_datasets/js-data/data/2021a_Wireline_Ethernet/data_beta.orc 2021a_Wireline_Ethernet" \
"scp solana@192.168.10.211:/data/Solana_datasets/js-data/data/2021c_Mobile_LTE/data_beta.orc 2021c_Mobile_LTE" \
"scp solana@192.168.10.211:/data/Solana_datasets/js-data/data/2022a_Wireline_Ethernet/data_beta.orc 2022a_Wireline_Ethernet" \
"scp solana@192.168.10.211:/data/Solana_datasets/js-data/data/2023a_Wireline_Ethernet/data_beta.orc 2023a_Wireline_Ethernet" \
"scp solana@192.168.10.211:/data/Solana_datasets/js-data/data/2023c_Mobile_LTE/data_beta.orc 2023c_Mobile_LTE" \
"scp solana@192.168.10.211:/data/Solana_datasets/js-data/data/2023e_MacOS_Wifi/data_beta.orc 2023e_MacOS_Wifi" \
"scp solana@192.168.10.211:/data/Solana_datasets/js-data/data/2024a_Wireline_Ethernet/data_beta.orc 2024a_Wireline_Ethernet" \
"scp solana@192.168.10.211:/data/Solana_datasets/js-data/data/2024ag_Wireline_Ethernet/data_beta.orc 2024ag_Wireline_Ethernet" \
"scp solana@192.168.10.211:/data/Solana_datasets/js-data/data/2024c_Mobile_LTE/data_beta.orc 2024c_Mobile_LTE" \
"scp solana@192.168.10.211:/data/Solana_datasets/js-data/data/2024cg_Mobile_LTE/data_beta.orc 2024cg_Mobile_LTE" \
"scp solana@192.168.10.211:/data/Solana_datasets/js-data/data/2024e_MacOS_Wifi/data_beta.orc 2024e_MacOS_Wifi" \
"scp solana@192.168.10.211:/data/Solana_datasets/js-data/data/Homeoffice2024a_Wireline_Ethernet/data_beta.orc Homeoffice2024a_Wireline_Ethernet" \
"scp solana@192.168.10.211:/data/Solana_datasets/js-data/data/Homeoffice2024ag_Wireline_Ethernet/data_beta.orc Homeoffice2024ag_Wireline_Ethernet" \
"scp solana@192.168.10.211:/data/Solana_datasets/js-data/data/Homeoffice2024c_Mobile_LTE/data_beta.orc Homeoffice2024c_Mobile_LTE" \
"scp solana@192.168.10.211:/data/Solana_datasets/js-data/data/Homeoffice2024e_MacOS_WiFi/data_beta.orc Homeoffice2024e_MacOS_Wifi" \
"scp solana@192.168.10.211:/data/Solana_datasets/js-data/data/Homeoffice2025cg_Mobile_LTE/data_beta.orc Homeoffice2025cg_Mobile_LTE" \
"scp solana@192.168.10.211:/data/Solana_datasets/js-data/data/Test2023a_Wireline_Ethernet/data_beta.orc Test2023a_Wireline_Ethernet" \
"scp solana@192.168.10.211:/data/Solana_datasets/js-data/data/Test2023c_Mobile_LTE/data_beta.orc Test2023c_Mobile_LTE" \
"scp solana@192.168.10.211:/data/Solana_datasets/js-data/data/Test2023e_MacOS_Wifi/data_beta.orc Test2023e_MacOS_Wifi" \
"scp solana@192.168.10.211:/data/Solana_datasets/js-data/data/Test2024a_Wireline_Ethernet/data_beta.orc Test2024a_Wireline_Ethernet" \
"scp solana@192.168.10.211:/data/Solana_datasets/js-data/data/Test2024ag_Wireline_Ethernet/data_beta.orc Test2024ag_Wireline_Ethernet" \
"scp solana@192.168.10.211:/data/Solana_datasets/js-data/data/Test2024c_Mobile_LTE/data_beta.orc Test2024c_Mobile_LTE" \
"scp solana@192.168.10.211:/data/Solana_datasets/js-data/data/Test2024cg_Mobile_LTE/data_beta.orc Test2024cg_Mobile_LTE" \
"scp solana@192.168.10.211:/data/Solana_datasets/js-data/data/Test2024e_MacOS_Wifi/data_beta.orc Test2024e_MacOS_Wifi"; do
    echo "Executing: $cmd"
    eval "$cmd"
    if [ $? -eq 0 ]; then
        echo "Command completed successfully"
    else
        echo "Command failed with exit code $?"
    fi
    echo "-----------------------------------"
done
