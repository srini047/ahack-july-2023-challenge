# ahack-july-2023-challenge

## Team Name
DevX

## Team members
- Sriniketh J ([@srini047](https://github.com/srini047))  `Sriniketh J#5743`
- Vignesh M ([@witviggy](https://github.com/witviggy))    `viggysprompt`


### Radar Plot
As the radar plot unfolds, we see a web of lines connecting various vertices, each representing a different attribute of the Pokemon`s stats.

![Radar plot](https://github.com/srini047/ahack-july-2023-challenge/assets/81156510/c3ba814c-5a8a-4c84-abf4-30ddc4b9d440)

### Contour Plot
Contour maps made with HP, Attack, Defense, Attack, Defense, and Speed ​​attributes provide an interesting insight into the Pokémon world. This graph focuses on the first 10 data points in the dataset.

![Contour Plot](https://github.com/srini047/ahack-july-2023-challenge/assets/81156510/9eb8e67f-d44f-4c8e-a198-2053cf2cb37c)

### Heat map Plot
The heatmap display shows a grid of color-coded cells, each representing the top 10 Pokémon. The X-axis shows the attributes (HP, Attack, Defense, Special Attack, Special Defense, and Speed) and the Y-axis shows the rank of those Pokémon.

<img width="713" alt="image" src="https://github.com/srini047/ahack-july-2023-challenge/assets/81156510/12941f52-aa6f-4c18-998a-6c8536b2d026">

### Dist Plot
The Attack/Defense chart of the Pokemon dataset provides valuable insight into the characteristics of Pokemon teams. By examining the distribution of attack and defense statistics, we can draw some important conclusions.

![Dist Plot](https://github.com/srini047/ahack-july-2023-challenge/assets/81156510/6cafb4ef-cc95-4315-b554-f3c432c5d66f)

### Scatter Plot 3D
Relates Average stats, Attack-Defense ratio, and Speed of all the Pokemon.

<img width="680" alt="image" src="https://github.com/srini047/ahack-july-2023-challenge/assets/81156510/7729a4d9-2897-47d0-a746-8b72ad74dd80">

### Top 10 Plot
The storyline features the top ten Pokémon characters based on their `overall` attributes, which generally measure a Pokémon`s overall power.

![Top 10 Plot](https://github.com/srini047/ahack-july-2023-challenge/assets/81156510/40476eec-8ed7-49e6-9bb2-d34df2756343)


## [dstack](https://dstack.ai) Integration

It is an open source platform that eases LLM  development on mutlitple cloud platforms. It supports Local, AWS, Azure, and GCP storage currently. This reduces the hassle of using costly development environment while running in the cloud. For this project we have utilized local storage since this does not require heavy GPU allocations and memory usage. Make sure that you have docker installed to run dstack locally.

### Step 1: Install and start the dstack server
```bash
pip3 install "dstack[aws,gcp,azure,lambda]"
dstack init
dstack start
```
[Docs](https://dstack.ai/docs/installation/pip/) for installation using `pip`. All three commands have to be run on the root of the folder, finally must provide the server response at the localhost:
<img width="810" alt="image" src="https://user-images.githubusercontent.com/81156510/255861931-cfc53976-04d0-4171-a47e-c8e4df778d29.png">

![Actual server](https://user-images.githubusercontent.com/81156510/255866875-a5acbd99-55d5-44b2-9f87-733170fc4c16.png)


### Step 2: Create the configuration file
Create a file named `serve.dstack.yml` and copy the contents below. This file serves as the base file for us to run the dstack commands and allocate the necessary resources. This looks very similar to the GitHub actions if you are familiar with it.

```yaml
type: task

env:
  - OPENAI_API_KEY=""

ports:
  - 8502

commands:
  - pip3 install -r requirements.txt 
  - streamlit run main.py
```

Then we have to use the following command to run the yml file:
```bash
dstack run . -f serve.dstack.yml --build --reload 
```
Parameters:
- `run` : Command that runs the configuration provided in the file
- `-f` : Refers to file
- `file_name.dstack.yml` : The actaul file that contains the commands to run
- `--build` : If the environment is not pre-built yet, pre-build it. If the environment is already pre-built, reuse it
- `--reload` : Since it is a Streamlit application and requires contious updates as and when we make changes

Sample terminal response:
https://user-images.githubusercontent.com/81156510/255859315-c0fc4bef-5282-446d-9262-4bba0914f0bc.mov

🎉 Now you have  successfully integrated dstack to your project using the local backend source.
