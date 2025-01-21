execute_command() {
    # Prompt the user for input
    echo -n "shllm> "
    read user_command < /dev/tty

    if [[ "$user_command" == "?" || "$user_command" == "help" ]]; then
      cat << 'EOHELP'
shllm: integrated LLM in your shell

To run press Ctrl+K or execute shllm cmd.

Examples:
1.
shllm> ffmpeg -i input.mp4 remove the audio and use the original video encoding

ffmpeg -i input.mp4 -c:v copy -an output.mp4


2.
shllm> remove the last line of the README.md file

sed -i '$d' README.md


3.
shllm> delete files that have two l's in their name

rm *l*l*


4.
shllm> htop sorted by most memory used

htop --sort-key=MEMORY

EOHELP
      exit
    fi

    llm_command=$(/usr/local/bin/core_shllm "$user_command")

    echo ""
    echo "$llm_command"
    echo ""
    echo "Press any key to run or Ctrl+C to abort"
    read key < /dev/tty

    echo "$llm_command" >> ~/.bash_history

    eval "$llm_command"

    history -r
}

# Call the function
execute_command
