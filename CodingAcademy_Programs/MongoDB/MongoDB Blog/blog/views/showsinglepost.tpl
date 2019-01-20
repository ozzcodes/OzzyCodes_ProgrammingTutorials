<!DOCTYPE html>
<html><head>
<title>List Blog Posts Page!</title>
</head>
<body>

<ul>
<li><a href="/">Home</a></li>
<li><a href="/list">List all posts</a></li>
</ul>

<h2>Post Subject:</h2>
{{post['title']}}

<h2>Text:</h2>
{{post['text']}}

<h2>Date written:</h2>
{{post['date']}}

</body></html>