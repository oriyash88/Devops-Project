# MemGenerator - React Meme Generator

MemGenerator is a React-based web application that allows users to generate and share memes easily. With MemGenerator, you can choose from a collection of popular meme templates, add your custom text, and create hilarious memes to share with your friends.

## Installation

1. Clone the repository:
git clone https://github.com/oriyash88/Devops-Project.git

2. Navigate to the project directory:
cd devops-test

3. Install the dependencies:

npm install

## Usage

1. Start the development server:

npm start


This will start the MemGenerator app on [http://localhost:3000] in your browser.

2. Use the MemGenerator interface to select a meme template, add your custom text, and customize the appearance.

3. Preview your meme and click on the download button to save it to your device.

4. Share your memes with your friends on social media platforms by uploading them directly or using the provided sharing options.

## React Meme Generator

The MemGenerator app is built with React and consists of the following components:

- **MemeGenerator**: This component handles the main functionality of the app. It fetches meme templates from an external API, allows users to input custom text, generates memes based on user input, and provides options for previewing and downloading the generated memes.

- **App**: This component serves as the entry point of the React app and renders the MemeGenerator component.

### Customization

- The MemGenerator app fetches meme templates from the [Meme API](https://meme-api.herokuapp.com/). You can modify the `componentDidMount` method in the `MemeGenerator` component (located in the `src/MemeGenerator.js` file) to fetch meme templates from a different API or data source if needed.

- The styling for the app can be customized by modifying the CSS in the `src/App.css` file.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please create an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- The meme templates used in this application are sourced from [Meme API](https://meme-api.herokuapp.com/).

<img width="1169" alt="image" src="https://github.com/mulatmek/devops-test/assets/89039091/394b77d0-e5cf-4636-bdf6-0a89dde5a404">

