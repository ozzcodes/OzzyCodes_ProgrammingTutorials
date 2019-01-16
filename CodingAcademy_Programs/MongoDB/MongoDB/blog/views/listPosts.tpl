<!DOCTYPE html>
<html><head>
<title>List Blog Posts Page!</title>
</head>
<body>

<ul>
<li><a href="/">home Page</a> </li>
<li><a href="/write">Write new post</a></li>
<li><a href="/login">User login (not implemented)</a></li>
<li><a href="/newuser">User Signup (not implemented)</a></li>
</ul>
	
<h1>This page shows all existing blog posts.</h1>

<ul>
%for myX in data:
<%
  link = str(myX['_id'])
%>
<li><a href="/post/{{link}}">{{myX['title']}}</a></li>
%end
</ul>

</body></html>