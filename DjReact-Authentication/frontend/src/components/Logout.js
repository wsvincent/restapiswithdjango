import React from 'react'
import axios from 'axios'
import {Link,Redirect} from 'react-router-dom'

class Logout extends React.Component {
	constructor(props) {
		super(props)
	
		this.state = {
			 context: {},
			 error: null
		}
	}
	componentDidMount() {
		const authAxios=axios.create({
			headers: {
				Authorization: `Token ${localStorage.getItem('token')}`
			}
		})
		authAxios.get('http://localhost:8000/logout/')
		localStorage.removeItem('token')
	}
	render() {
		return <Redirect to="/login/" />
	}
}

export default Logout