import React from 'react';
import axios from 'axios';
import {Link,Redirect} from 'react-router-dom';

class Register extends React.Component {
	constructor(props) {
		super(props)
	
		this.state = {
			 context: {},
			 email: "",
			 username: "",
			 password1: "",
			 password2: "",
			 error: null,
			 token: "",
			 authenticated: false
		}
	}

	componentDidMount = ()=>{
		axios.get('http://localhost:8000/register/')
		.then(
			(response)=>{
				this.setState({context: response.data})
				console.log(this.state.context)
			}
		)
		.catch(
			(error)=>{
				this.setState({error: error.response})
				console.log(this.state.error)
			}
		)
		
	}

	changeHandler = (e)=>{
		this.setState({
			[e.target.name]: e.target.value
		})
	}

	submitHandler = (e)=>{
		e.preventDefault()
		let form={}
		form.email=this.state.email
		form.username=this.state.username
		form.password1=this.state.password1
		form.password2=this.state.password2

		axios.post('http://localhost:8000/register/',form)
		.then(
			(response)=>{
				this.setState({
					token: response.data.token,
					context: response.data,
				})
				delete this.state.context.token
				if(this.state.token){
					this.setState({authenticated:true})
				}
				console.log(response)
			}
		)
		.catch(
			(error)=>{
				this.setState({error:error.response})
				console.log(this.state.error)
			}
		)

	}

	formErrors = ()=>{
		let {error}=this.state
		if(error){
			return (
				<React.Fragment>
					<br/>
					<div className="row">
							<div className="col" />
							<div className="alert alert-danger col" type="submit">
								{error.data.errMsg}
							</div>
							<div className="col" />
						</div>
					</React.Fragment>
			)
		}
	}

	render() {
		let {username,email,password1,password2,authenticated} = this.state
		if (authenticated){
			localStorage.setItem('token',this.state.token)
			return <Redirect to="/" />
		}
		if (localStorage.getItem('token')){
			return <Redirect to="/" />
		}
		return (
			<React.Fragment>
				<center>
					<h4>Registeration Form</h4>
				</center>
				<br/>
				<form className="form-group" onSubmit={this.submitHandler}>
					<div className="row">
						<div className="col" />
						<input 
							name="email" 
							type="email" 
							className="form-control col"
							onChange={this.changeHandler}
							value={email}
							placeholder="E-mail"
							required
						/>
						<div className="col" />
					</div>
					<div className="row">
						<div className="col" />
						<input 
							name="username" 
							type="text" 
							className="form-control col"
							onChange={this.changeHandler}
							value={username}
							placeholder="Username"
							required
						/>
						<div className="col" />
					</div>
					<div className="row">
						<div className="col" />
						<input 
							name="password1" 
							type="password"
							className="form-control col"
							onChange={this.changeHandler}
							value={password1}
							placeholder="Password"
							required
						/>
						<div className="col" />
					</div>
					<div className="row">
						<div className="col" />
						<input 
							name="password2" 
							type="password"
							className="form-control col"
							onChange={this.changeHandler}
							value={password2}
							placeholder="Confirm Password"
							required
						/>
						<div className="col" />
					</div>
					<div className="row">
						<div className="col" />
						<button className="btn btn-primary col" type="submit">
							Register
						</button>
						<div className="col" />
					</div>
					<br/>
					<div className="row">
						<div className="col" />
						<Link to="/login">
							Login
						</Link>
						<div className="col" />
					</div>
					{this.formErrors()}
				</form>
			</React.Fragment>
		)
	}
}

export default Register