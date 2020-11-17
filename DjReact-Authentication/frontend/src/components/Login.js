import React from 'react';
import axios from 'axios';
import {Link,Redirect} from 'react-router-dom';



class Login extends React.Component {
	constructor(props) {
		super(props)
	
		this.state = {
			context: {},
			username: "",
			password: "",
			token: "",
			error: null,
			authenticated: false
			 
		}
	}
	componentDidMount = ()=>{
		axios.get('http://localhost:8000/login/')
		.then(
			(response)=>{
				this.setState({context:response.data})
				console.log(this.state.context)
			}
		)
		.catch(
			(error)=>{
				this.setState({error:error.response})
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
		form.username=this.state.username
		form.password=this.state.password
		axios.post('http://localhost:8000/login/',form)
		.then(
			(response)=>{
				this.setState({
					token: response.data.token,
					authenticated: true
				})
			}
		)
		.catch(
			(error)=>{
				this.setState({
					error:error.response,
					authenticated: false
				})
				
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
		let {username,password,authenticated}=this.state
		if(authenticated){
			localStorage.setItem('token',this.state.token)
			return <Redirect to="/" />
		}
		return (
			<React.Fragment>
				<center>
					<h4>Login Form</h4>
				</center>
				<br/>
				<form className="form-group" onSubmit={this.submitHandler}>
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
							name="password" 
							type="password"
							className="form-control col"
							onChange={this.changeHandler}
							value={password}
							placeholder="Password"
							required
						/>
						<div className="col" />
					</div>
					<div className="row">
						<div className="col" />
						<button className="btn btn-primary col" type="submit">
							Login
						</button>
						<div className="col" />
					</div>
					<br/>
					<div className="row">
						<div className="col" />
						<Link to="/register">
							Register
						</Link>
						<div className="col" />
					</div>
					{this.formErrors()}
				</form>
			</React.Fragment>
		)
	}
}

export default Login