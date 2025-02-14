
# Blog Generator App

This is a Streamlit-based application that leverages the Hugging Face transformers library to generate blogs based on a given topic, word count, and target audience. The app uses the GPT-2 model for text generation.


## Features

- User-friendly Streamlit interface

- Accepts blog topic input

- Allows customization of word count

- Supports different writing styles: Researchers, Data Scientists, and Common People

- Uses Hugging Face's GPT-2 model for blog generation

- Generates text dynamically with AI-powered capabilities

- Provides instant results with minimal user input

## Installation

Prerequisites

Ensure you have Python installed (Python 3.7 or later is recommended). Install the required dependencies using:

```bash
  pip install streamlit transformers torch
```
    
## Usage

1.Run the Streamlit app:

```bash
streamlit run app.py
```
2.Enter a blog topic in the text input field.

3.Specify the number of words for the blog.

4.Select the target audience from the dropdown menu.

5.Click on the "Generate" button to generate the blog content.

6.Review the generated blog and refine inputs as needed.
## How It Works

1.User Input: The user provides a topic, selects a target audience, and specifies a word limit.

2.Text Generation: The GPT-2 model processes the input and generates a blog based on the given constraints.

3.Output Display: The generated content is displayed in the Streamlit interface, ready for further refinement or usage.
## Dependencies

- streamlit

- transformers

- torch
## Customisations

- You can modify the model used by changing model="gpt2" to another pre-trained model available on Hugging Face.

- Adjusting max_new_tokens allows for better control over the blog length.

- The user interface can be customized in Streamlit to enhance usability.
## Notes

- The application uses the GPT-2 model, which is a publicly available language model from Hugging Face.

- The device=-1 setting ensures the model runs on the CPU. If using a GPU, modify this to device=0.

- The generated text may require minor editing for coherence and readability.
## Future Enhancements

- Support for additional AI models such as GPT-3 or Llama models.

- Improved customization options for writing styles.

- Integration with external APIs for enhanced text quality.

- Option to download the generated blog as a text or markdown file.
## License
This project is licensed under the MIT License.
[MIT](https://choosealicense.com/licenses/mit/)


## Contributing

Contributions are welcome! If you'd like to improve the project, please submit a pull request or open an issue on GitHub.

