## Intro

- Burp Proxy
- Firefox

- First Bug
```php
if (isset($_GET['name'])) {
    echo "<h1>Hello {$_GET['name']}</h1>";
}

<form method="GET">
    Enter your name: <input type="input" name="name"><br>
    <input type="submit">
</form>
```

If I put hoge.com/page.php?name=<script>alert(1);</script>??
This is Reflected XSS's example. 

