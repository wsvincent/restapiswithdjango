import React from 'react'
import {Link,Redirect} from 'react-router-dom'
import axios from 'axios'

class Home extends React.Component {
	constructor(props) {
		super(props)
	
		this.state = {
			context:{},
			error:'',
			authenticated: true
		}
	}

	componentDidMount = ()=>{
		let authAxios=axios.create({
			headers: {
				Authorization: `Token ${localStorage.getItem('token')}`
			}
		});
		authAxios.get('http://localhost:8000/')
		.then(
			(response)=>{
				this.setState({
					context:response.data,
					authenticated: true
				})
				console.log(this.state.context)
			}
		)
		.catch(
			(error)=>{
				this.setState({
					error:error.message,
					authenticated: false
				})
				console.log(this.state.error)
			}
		)
	}

	render() {
		let {context,error,authenticated}=this.state
		if (!authenticated){
			return(
				<Redirect to="/login" />
			)
		}
		return (
			<React.Fragment>
				<div className="row">
					<div className="col" />
					<div className="col">
						<p className="lead">
						Title: {context.title}
						<br/>
						User: {context.username}
						</p>
					</div>
					<div className="col" />
				</div>
				<div className="row">
					<div className="col" />
					<Link to="/logout" className="col">
						<button className="btn btn-outline-primary col">Logout</button>
					</Link>
					<div className="col" />
				</div>
			</React.Fragment>
		)
	}
}

export default Home