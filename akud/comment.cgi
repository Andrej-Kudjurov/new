#!/usr/bin/perl

use CGI;
$query = new CGI;
if ($query->param)
{
	$name=$query->param(login);
	@t=localtime();
	$toc="($t[2]:$t[1]:$t[0] $t[3]/".($t[4]+1)."/".($t[5]+1900).")";
	$comhead="<tr><td><b>$name</b> at $toc</td></tr>";
	$comment=$query->param(comment);
	@check=split(/ /,$comment);
	$flag=0;
	@check=split(/ /,$comment);
	for (my $i=0; $i < scalar(@check); $i++)
	{
		if (length($check[$i])>60)
		{
			$flag=1;
			my @strbuf=split(//,$check[$i]);
			for (my $i1=0; $i1 < scalar @strbuf; $i1+=60)
			{
				if (defined($strbuf[$i1+60])){$strbuf[$i1+60]=" "};
			}
			$check[$i]=join(/""/,@strbuf);
		}
	}
	if ($flag==1){$comment=join(/" "/,@check);}
	$com="<tr><td><i>$comment</i></td></tr>";
	$stp=$comhead."\n".$com."\n".qq|<tr><td align="center"><p></td></tr>|;
	$buf="";
	if (open($fh,"<", "com.dat"))
	{
		while (<$fh>)
		{$buf.=$_;}
		close($fh);
	}
	open($fh,">", "com.dat");
	print $fh $stp,$buf;
	close($fh);
}
print "Content-Type: text/html\n\n";
print <<"HTML"
<HTML>
<HEAD>
<META HTTP-EQUIV="REFRESH" CONTENT="3; URL=/akud/index.cgi">
</HEAD>
<BODY>
<center>
<table width="800" border="1">
<tr><td align="center"><h2>������� �� ��� �����������</h2><p>������ �� ������ �������������� � �������� �����</td></tr>
</table>
</center>
</BODY>
</HTML>
HTML
;
