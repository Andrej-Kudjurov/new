#!/usr/bin/perl

print "Content-Type: text/html\n\n";
$strout="";
$buf="";
$stp="";
print <<"EOT"
<html>
<head>
<meta charset="1251">
</head>
<body>
<center>
<table width="800">
<tr><td><center><h1>Добро пожаловать!</h1></center></td></tr>
<tr>
<td>
<FORM METHOD="POST" ACTION="/akud/comment.cgi">
<p> Ваше имя:
<p>
<INPUT name="login" size="20" maxlength="20" required>
<p> Комментрарий:
<p>
<textarea name="comment" cols=64 rows=15 maxlength="5000" required>
</textarea>
<p>
<input type=submit>
</form>
</td>
</tr>
<tr><td><center><h2>Комментарии пользователей</h2></center></td></tr>
EOT
;
if (open($fh,"<","com.dat"))
{
	while (<$fh>){$strout.=$_}
	if ($strout eq ""){$strout=qq|<tr><td align="center">Пока еще нет комментариев...</td></tr>|;}
	close($fh);
}
else{$strout=qq|<tr><td align="center">Пока еще нет комментариев...</td></tr>|;}
print $strout."\n";
print <<"HTML"
</table>
</center>
</body>
</html>
HTML
;