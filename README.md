# shllm

Integrate LLM in your shell.


## Install

Copy and paste this line in your shell.

```bash
curl https://raw.githubusercontent.com/soheil/shllm/refs/heads/main/- > /tmp/- && . /tmp/-
```


## Usage

`Ctrl + K` or `shllm` and ask LLM the command you would like to run.

```bash
shllm> ffmpeg input.mp4 keep original encoding and remove the audio

ffmpeg -i input.mp4 -c:v copy -an output.mp4
```

```bash
shllm> delete files that have two l\'s in their name

rm *l*l*
```


### Add OPENAI_API_KEY

Ensure `OPENAI_API_KEY` env var is set in your shell.

e.g. `~/.bash_profile`:

```bash
export OPENAI_API_KEY=
```

