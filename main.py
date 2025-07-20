import gradio as gr


def main() -> None:
    i18n: gr.I18n = gr.I18n(
        en={
            "input_text": "Input Text",
            "formatting_options": "Formatting Options",
            "select_formatting": "Select Formatting Options",
            "bold": "Bold",
            "italic": "Italic",
        }
    )

    def demo_fn(input: str, format: list[str]) -> str:
        if "bold" in format:
            input = f"**{input}**"
        if "italic" in format:
            input = f"_{input}_"
        return input

    demo: gr.Interface = gr.Interface(
        fn=demo_fn,
        inputs=[
            gr.Textbox(label=i18n("input_text")),
            gr.CheckboxGroup(
                label=i18n("formatting_options"),
                choices=[
                    (i18n("bold"), "bold"),
                    (i18n("italic"), "italic"),
                ],
                info=i18n("select_formatting"),
            ),
        ],
        outputs=gr.Markdown(),
    )

    demo.launch(server_name="localhost", i18n=i18n)


if __name__ == "__main__":
    main()
