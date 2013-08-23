#!/usr/bin/perl

%h=('0'=>'','1'=>'checked');
$ind = int(rand(2));
$ch = int(rand(2));
if ($ind == 0){$expr = qq|<input type="checkbox" name="bots" value="not" $h{$ch}> Я не спам-бот|; $val = '1';}
else{$expr = qq|<input type="checkbox" name="bots" value="bot" $h{$ch}> Я - спам-бот|; $val = '0';}

print "content-type: text/html\n\n";
print <<"HTML"
	<html>
	<head>
	<meta charset="utf-8">
	</head>
	<center>
	<table width="800">
	<tr>
	<bt></br>
	<td>
	</td>
	<td>
	<h2>Почтовый экспресс</h2>
	<br></br>
	<h3>Заполните форму отправки</h3>
	<BR></BR>
	</td>
	<form method="post" action="/akud2/mail.cgi">
	<tr>
	<td>
	E-mail отправителя:
	</td>
	<td>
	<input name="email" size="30" maxlength="50" required>
	</td>
	</tr>
	<tr>
	<td>
	Тема:
	</td>
	<td>
	<input name="subj" size="30" maxlength="300" required>
	</td>
	</tr>
	<tr>
	<td valign="top">
	Сообщение:
	</td>
	<td>
	<textarea name="content" cols="64" rows="12" required>
	</textarea>
	</td>
	</tr>
	<tr>
	<td>
	</td>
	<td>
	$expr
	<br></br>
	<input type="hidden" name="val" value="$val">
	<input type="submit" value="Отправить">
	</td>
	</tr>
	</form>
	</table>
	</center>
	</body>
	</html>
HTML
;