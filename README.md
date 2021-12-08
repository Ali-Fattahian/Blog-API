<h2>This Blog API is Based on my Techie-Tweed Blog</h2> <a href="https://techie-tweed.herokuapp.com">Techie Tweed</a><br><hr>

<h3>this api uses jwt-token authentication. i also added session-based auth just in case</h3>
<h3>for handling authentication/authorization i used two awesome packages : <a href="https://django-rest-framework-simplejwt.readthedocs.io/en/latest/">Simple JWT</a> and <a href="https://djoser.readthedocs.io/en/latest/introduction.html">Djoser</a></h3>
<hr>
<h4>Here is the list of all available urls for this api :</h4>
<h5> /api/posts : to see all the existing posts and also to add a new post if you have the permission</h5>
<h5> /api/posts/slug : to see details of a post and change or delete it if you are the author</h5>
<h5> /api/posts/slug/comments : to see all the comments for that post and add a comment if you are authenticated</h5>
<h5> /api/posts/slug/comments/pk : to see a specific comment by its id and change or delete it if you are the author</h5><br>
<h5> /api/tags : to see all the existing tags and also to add a new tag if you have the permission </h5>
<h5> /api/tags/pk : to see a specific tag by its id and change or delete it if you are the creator </h5><hr>
<h4>**and as for auth everything is in <a href="https://djoser.readthedocs.io/en/latest/getting_started.html#available-endpoints">Djoser docs website</a>. <bold>JUST add auth/ before all of them**</bold></h4>
