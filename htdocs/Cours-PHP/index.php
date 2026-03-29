<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Cours PHP</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <?php
            $ma_var = 58;
            echo "<h1>Hello world</h1>";
            echo "<h2>Définition d'une variable</h2>";
            echo '<p>$var = value;<br>';
            echo "Par exemple \$var = $ma_var;</p>";
        ?>

        <form action="" method="POST">
            <label for="1">Anime 1</label>
            <input type="radio" name="anime" value="1" id="1">

            <label for="2"><br>Anime 2</label>
            <input type="radio" name="anime" value="2" id="2">

            <br><br>
            <button type="submit">Envoyer</button>

            <?php
                if (isset($_POST["anime"])) {
                    $choix = $_POST["anime"];
                    echo "<p>Votre choix: Anime numero $choix</p>";
                }
            ?>
        </form>

        <p>
            Pour faire une requête SQL :<br>
            <code>$result = $dbh->query("SELECT nameCol FROM table");</code>
        </p>

    </body>
</html>