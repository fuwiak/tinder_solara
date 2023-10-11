import solara


key = solara.reactive("sk-")  # Query
temperature = solara.reactive(0.5)  # Subreddit
prompt = solara.reactive("I am a highly intelligent robot")  # Subreddit

@solara.component
def Page():
    solara.Markdown("## Welcome to Solara")
    with solara.Sidebar():
        solara.Markdown("### Sidebar")

        solara.Markdown("#### InputText")
        solara.InputText("Put OpenAI API key here", value=key.value)

        solara.Markdown("#### Temperature of model")
        solara.SliderFloat(label="Temperature", value=temperature, min=0.0, max=1.0)
        solara.Markdown(f"**You entered**: {temperature.value}")


        solara.Markdown("#### Prompt")
        solara.InputText("Enter a prompt", value=prompt.value)


    #text fied for output
    solara.Markdown("#### Output")
    solara.Text("Output will be here")





Page()

