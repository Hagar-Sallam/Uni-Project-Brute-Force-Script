<?php

if (isset($_POST['login'])) {
// the expression isset($_POST['Submit']) return true only if 'Submit' is an existing parameter,
// i.e. if the user has sent such a value using n HTML form
  $username = "";
  $password = "";

  $db = mysqli_connect('localhost', 'root', '', 'credentials');
  // connects to the database

  if (mysqli_connect_errno()) {
    //checks if any connection error was found
    echo "Failed to connect to MySQL: " . mysqli_connect_error();
    exit();
  }

  if (empty($_POST['username']) || empty($_POST['password'])) {
    // check if username or password fields in the form is empty
    echo ('Please fill all required fields!');
    exit();
  }

  $username = mysqli_real_escape_string($db, $_POST['username']);
  $password = mysqli_real_escape_string($db, $_POST['password']);
  //it removes any special characters that may interfere with the query operations.

  $user_check_query = "SELECT * FROM credentials WHERE Username='$username' AND Password='$password'";
  // SQL query
  $result = mysqli_query($db, $user_check_query);
  //Execution of the query
  $user = mysqli_fetch_assoc($result);
  //user is an array having the result
  if ($user) // if such a user was found redirect to home page
    header("Location: home.php");
  else
      echo ("Wrong username or password");
}

