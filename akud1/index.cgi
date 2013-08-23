#!/usr/bin/perl

use CGI;
$query = new CGI;
$name = $query->cookie('akud_name');
$pass = $query->cookie('akud_pass');
if ($query->param)
{
	$c1 = $query->cookie(-name=>'akud_name', -value=>$name, -expires=>'-1h');
	$c2 = $query->cookie(-name=>'akud_pass', -value=>$pass, -expires=>'-1h');
	print $query->header(-cookie=>[$c1,$c2],-type=>'text/html',-charset=>'utf-8');
	$name = '';
	$pass = '';
}

if (!$query->param){print "Content-Type: text/html\n\n";}

print <<"HTML"
<html>
<head>
<meta charset="utf-8">
</head>
<body>
<center>
<table width="300" border="1" cellspacing="3">
<tr>
<td align="center" valign="center">
<br>
<b>Войдите или зарегистрируйтесь</b>
<p>
</td>
</tr>
<tr>
<td>
<table>
<form method="post" action="/akud1/quote.cgi">
<tr>
<td width="70" valign="top">
Логин:
<p> 
Пароль:
</td>
<td valign="top">
<input name="login" size="20" maxlength="20" value='$name' required>
<P>
<input name="pass" type="password" size="20" maxlength="20" value='$pass' required>
<p>
<input type="radio" name="coo" value="1">cookie
<input type="radio" name="coo" value="0" checked>hidden
<p>
<input type="submit" value="Вход">
</td>
</tr>
</form>
</table>
</td>
</tr>
<tr>
<td>
<table>
<form method="post" action="/akud1/quote.cgi">
<tr>
<td width="70" valign="top">
Логин:
<p> 
Пароль:
<p>
Проверка пароля:
</td>
<td valign="top">
<input name="login" size="20" maxlength="20" required>
<P>
<input name="pass" type="password" size="20" maxlength="20" required>
<p>
<input name="rpass" type="password" size="20" maxlength="20" required>
<p>
<input type="radio" name="coo" value="1">cookie
<input type="radio" name="coo" value="0" checked>hidden
<p>
<input type="submit" value="Регистрация">
</td>
</tr>
</form>
</table>
</td>
</tr>
</table>
</center>
</body>
</html>
HTML
;