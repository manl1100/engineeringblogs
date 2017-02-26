import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import BlogList from './BlogList';

class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="App-header">
          <span>S.E. Things</span>
        </div>
        <div className="content">
          <BlogList />   
        </div>
      </div>
    );
  }
}

export default App;
