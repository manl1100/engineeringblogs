import React, { Component } from 'react'
import { Card, Icon, Image } from 'semantic-ui-react'
import './BlogList.css';

class BlogList extends Component {

	constructor(props) {
	    super(props);
	    this.state = {
	    	blogs: []
	    }
  	}

	componentWillMount() {
		var myHeaders = new Headers();

		var myInit = {
		  method: 'GET',
		  headers: myHeaders,
		  cache: 'default'
		};

	fetch('http://localhost:8888/blogs', myInit)
	  .then((response) => {
	    if (response.status !== 200) {
	      console.log("Problem status: ", response.status);
	      return;
	    }

	    response.json().then((response) => {
	      this.setState({ blogs: response })  
	    }); 
	  })
	  .catch((err) => {
	    console.log("Fetch Error: ", err)
	  })
	}

	getInitialState() {
		return {
			blogs: []
		};
	}

	render() {
		return (
			<Card.Group>
				{this.state.blogs.map(function(blog) {
					return (
						<Card className="flat" href={blog.url} key={blog.id}>
					    	<Image className="thumbnail" src={blog.thumbnail} />
						    <Card.Content>
						      <Card.Header>
						        {blog.title}
						      </Card.Header>
						      <Card.Meta>
						        <span className='date'>
						          {blog.company}
						        </span>
						      </Card.Meta>
						      <Card.Description>
						      </Card.Description>
						    </Card.Content>
					  	</Card>
					  	)
				})}
			</Card.Group>)
		}
}

export default BlogList