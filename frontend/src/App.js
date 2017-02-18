import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import BlogList from './BlogList';

class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
        </div>
        <div className="content">
          <BlogList />   
        </div>
      </div>
    );
  }
}

export default App;
