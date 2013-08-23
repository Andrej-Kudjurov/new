#!/usr/bin/perl

use CGI;
my $query = CGI->new;

my $email = $query->param(email);
my $subj = $query->param(subj);
my $content = $query->param(content);
my $val = $query->param(val);
my $bots = $query->param(bots);

my $flag = 1;
my $out = '';

if (!($email=~/^[\w\.-]+\@[\w\.-]+$/)){$flag = 0; $out = '<b>Ошибка!</b><br></br>Неправильный адрес';}
if ((!$bots and $val == 1) or ($bots and $val == 0))
{$flag = 0; $out = '<b>Ошибка!</b><br></br>Обслуживание спам-ботов временно приостановлено';}

if ($flag == 1)
{
	open (SENDMAIL, "|/usr/sbin/sendmail -t");
	print SENDMAIL "From: $email\n";
	print SENDMAIL "To: student\@localhost\n";
	print SENDMAIL "Subject: $subj\n\n";
	print SENDMAIL "$content\n";
	close(SENDMAIL);
	$out = '<br></br>Сообщение отправлено!';
}



print "content-type: text/html\n\n";
print <<"HTML"
<html>
<head>
<meta charset = "utf-8">
</head>
<body>
<center>
<table border = "1" width="300">
<tr>
<td align = "center">
$out
<br></br>
<a href="/akud2/index.cgi">Назад</a>
<br></br>
</td>
</tr>
</table>
</center>
</body>
</html>
HTML
;