<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

  <title>Print my recipie</title>

  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
  <link href="styles.css" rel="stylesheet">

</head>
<body class="text-center">
    <form class="form-signin" method="post" action="print_submit.php">
      <img class="mb-4" src="../../assets/brand/bootstrap-solid.svg" alt="" width="72" height="72">
      <h1 class="h3 mb-3 font-weight-normal">Paste a BBC Good Food URL to print the recipie for!</h1>
      <label for="inputEmail" class="sr-only">URL</label>
      <input type="url" name='URL-from-user' id="inputEmail" class="form-control" placeholder="URL goes here" required autofocus>
      <button class="btn btn-lg btn-primary btn-block" type="submit" onclick="">Print</button>
      <p class="mt-5 mb-3 text-muted">&copy; Ya Boi Jake 2018</p>
    </form>

  </body>
</html>