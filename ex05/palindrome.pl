#!/usr/bin/perl

print "Enter a string: ";
my $string = <STDIN>;
chomp $string;  # 입력값에서 개행 문자 제거

# string이 회문일때
if ($string eq reverse $string)
{
	print "The string is a palindrome!\n";
}
else
{
	print "The string is not a palindrome!\n";
}
