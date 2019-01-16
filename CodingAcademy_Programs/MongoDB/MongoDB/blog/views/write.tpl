<!DOCTYPE html>
<html><head>
<title>Write a Blog Post.</title>
</head>
<body>

<h2>If you do not want to write a new post select one of the following:</h2>

<ul>
<li><a href="/">home Page</a> </li>
<li><a href="/list">List all posts</a></li>
<li><a href="/login">User login (not implemented)</a></li>
<li><a href="/newuser">User Signup (not implemented)</a></li>
</ul>
	
<form action="/presentnewpost" method="POST">
	
<h2>Subject:</h2>
<input type="text" name="subject" size="120" value="{{subject}}"><br>
<h2>Blog Text:<h2>
<textarea name="body" cols="120" rows="20">{{body}}</textarea><br><p>
<input type="submit" value="Submit">

</body></html>