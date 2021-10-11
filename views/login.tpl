<html lang="en">
<style>
%include views/css/login-page-css.tpl
</style>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <title>ALI</title>
  <meta name="description" content="A simple HTML5 Template for new projects.">
  <meta name="author" content="SitePoint">

  <meta property="og:title" content="A Basic HTML5 Template">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://www.sitepoint.com/a-basic-html5-template/">
  <meta property="og:description" content="A simple HTML5 Template for new projects.">
  <meta property="og:image" content="image.png">

  <link rel="shortcut icon" type="image/x-icon" href="static\icon.ico">  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  

  <link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@300&amp;display=swap" rel="stylesheet">
</head>

<body>
<form action="/" method="post"> 
    <div class="main-wrapper">
      <div class="small bubble"></div>
      <div class="large bubble"></div>
      <img src="static\logo.png" alt="logo">
      <i class="fas fa-user"></i> 
      <input type="text" placeholder="Username" name="username" class="text">      
      <input type="text" placeholder="Password" name="password" class="text"> 

      <input type="button" value="Login" class="button">

      <p>Don't have an account or forgot password?</p> 
      <p>Please contact ALI support.</p>
    </div>
</form>

    <script src="Scripts/login-page.js"></script>
    <script src="https://code.jquery.com/jquery-3.6.0.js"
            integrity="sha256-H+K7U5CnXl1h5ywQfKtSj8PCmoN9aaq30gDh27Xc0jk="
            crossorigin="anonymous">
    </script>
</body>
</html>