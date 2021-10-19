<html lang="en">
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

  <link rel="shortcut icon" type="image/x-icon" href="static\images\icon.ico">  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <link rel="stylesheet" href="static/css/login-page.css">

  <link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@300&amp;display=swap" rel="stylesheet">
</head>

<body>
<form action="/" method="post"> 
    <div class="main-wrapper">
      <div class="small bubble"></div>
      <div class="large bubble"></div>
      <img src="static\images\logo.png" alt="logo">
      <i class="fas fa-user"></i> 

      % if failedLogin:
        <p style="color: red">Failed log</p>
      %end

      <input type="text" placeholder="Username" name="username" class="text">      
      <input type="text" placeholder="Password" name="password" class="text" > 

      <input type="submit" value="Login" class="button">

      <p>Don't have an account? <a href="/signup">Sign Up</a></p> 
    </div>
</form>

    <script src="static/scripts/login-page.js"></script>
    <script src="https://code.jquery.com/jquery-3.6.0.js"
            integrity="sha256-H+K7U5CnXl1h5ywQfKtSj8PCmoN9aaq30gDh27Xc0jk="
            crossorigin="anonymous">
    </script>
</body>
</html>
