import React, { Component } from 'react'
import { Item } from 'semantic-ui-react'

class BlogList extends Component {

	constructor(props) {
	    super(props);
	    this.state = {
	      blogs: []
	    };
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
	      this.setState({ blogs: response.data })  
	    }); 
	  })
	  .catch((err) => {
	    console.log("Fetch Error: ", err)
	  })
	}

	render() {
		return (
			<Item.Group divided link>
				{this.state.blogs.map(function(blog) {
		              return (
		              	<Item href={blog.url}>
		              		<Item.Image size='large' src={blog.thumbnail}/>
		              		<Item.Content verticalAlign='middle'>
		              			<Item.Header as='a'>{blog.title}</Item.Header>
		              			<Item.Meta>
		              				<Item.Description>{blog.company}</Item.Description>
		              			</Item.Meta>
		              			<Item.Extra>Additional Details</Item.Extra>
		              		</Item.Content>
		              	</Item>
		              )
	          	})}
		    </Item.Group>
	    )
	}
}

export default BlogList