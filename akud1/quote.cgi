#!/usr/bin/perl
use DBI;
use CGI;
my $dsn = "DBI:mysql:database=test; host=localhost; port=3306";
my $dbh = DBI->connect($dsn,"root","PerlStudent");
$dbh->do("create table if not exists myusr(name varchar(21), password varchar(21), numb int(8)) charset='utf8' engine=myisam;");
my $query = new CGI;
my $flag = 0;
$errdesc = "";
our $qnum;
my $login = $query->param(login);
my $pass = $query->param(pass);


if ($query->param(quote))
{
	$flag = 2;
	use LWP::Simple;
	$qnum = $query->param(quote);
	my $url = "http://bash.org/?$qnum";
	my $resp = get($url) || $flag==0;
	if ($flag == 2)
	{
		my $tnum = $qnum;
		$qnum+=1;
		$dbh->do(qq|update myusr set numb = '$qnum' where name = '$login';|);
		$resp =~ s/.*\<p class="qt">//gs;
		$resp =~ s/\<\/p\>.*//gs;
		print "content-type: text/html\n\n";
		print <<"HTML"
		<html>
		<head>
		<meta charset="utf-8">
		</head>
		<body>
		<center>
		<table width="600" cellspacing="5">
		<tr>
		<td align="center">
		#$tnum
		<br></br>
		<p>
		<p>
		***
		</td>
		</tr>
		<tr>
		<td>
		<p>
		$resp
		<br></br>
		<form method="post" action="/akud1/quote.cgi">
		<input type="hidden" name="login" value="$login">
		<input type="hidden" name="pass" value="$pass">
		<input type="hidden" name="quote" value='$qnum'>
		<input type="submit" value="дальше">
		</form>
		<p>
		<form method="post" action="/akud1/index.cgi">
		<input type="submit" value="домой">
		</form>		
		<br></br>
		<form method="post" action="/akud1/index.cgi">
		<input type="hidden" name="ex" value="1">
		<input type="submit" value="выход">
		</form>
		</td>
		</tr>
		</table>
		</center>
		</body>
		</html>
HTML
;
	}
	
}
elsif ($query->param(rpass))
{
	if ($query->param(rpass) eq $pass)
	{
		my $sth = $dbh->prepare(qq|select name from myusr where name = '$login';|);
		my $state = $sth->execute();
		if ($state==0)
		{
			$dbh->do(qq|insert into myusr (name,password,numb) VALUES('$login', '$pass', '8')|);
			$flag = 1;
			$qnum = 8;
		}
		else{$errdesc = "Пользователь с именем $login уже существует";}
	}
	else{$errdesc = "Пароли не совпадают";}
}
elsif ($query->param(pass))
{
	my $sth = $dbh->prepare(qq|select numb from myusr where name = '$login' and password = '$pass';|);
	my $state = $sth->execute();
	if ($state!=0)
	{
		@ans=$sth->fetchrow_array;
		$qnum = $ans[0];	
		$flag = 1;
	}
	else{$errdesc = "Неверный логин или пароль";}
}
if ($flag==1 and $query->param(coo)==1)
{
	$c1 = $query->cookie(-name=>"akud_name",-value=>"$login");
	$c2 = $query->cookie(-name=>"akud_pass",-value=>"$pass");
	print $query->header(-cookie=>[$c1,$c2],-type=>'text/html',-charset=>'utf-8');
}
elsif (($flag==0 or $query->param(coo)==0) and $flag!=2){print "Content-Type: text/html\n\n";}


#IF error
if ($flag==0)
{
	if ($errdesc eq ""){$errdesc = "Неизвестная ошибка";}
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
	<b>Ошибка</b>
	<p>
	<i>$errdesc</i>
	<br></br>
	<a href="/akud1/index.cgi">На главную</a>
	</td>
	</tr>
	</table>
	</center>
	</body>
	</html>
HTML
;
}

#IF success
if ($flag == 1)
{
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
	Вы вошли как <b>$login</b>
	<p>
	<form method="post" action="/akud1/quote.cgi">
	<input type="hidden" name="login" value="$login">
	<input type="hidden" name="pass" value="$pass">
	<input type="hidden" name="quote" value='$qnum'>
	<input type="submit" value="начать просмотр">
	<br></br>
	<a href="/akud1/index.cgi">Войти под другим именем</a>
	</td>
	</tr>
	</table>
	</center>
	</body>
	</html>
HTML
;
}


$query = undef;