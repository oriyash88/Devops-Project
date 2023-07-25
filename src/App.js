import React from 'react';
import MemeGenerator from './MemeGenerator'
import Header from './Header'
import './App.css';

function App() {
	return (
		<div className="App">
			<Header/>
			<MemeGenerator />
		</div>
	);
}

export default App;
