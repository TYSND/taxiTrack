<?php
require 
class taxiInfoDAO
{
	public function select($str)
	{
		$mh=new mysqlHelper();
		return $mh->executeSql($str);
	}
	public function insert($str)
	{
		$mh=new mysqlHelper();
		return $mh->executeSql($str);
	}
	public function update($str)
	{
		$mh=new mysqlHelper();
		return $mh->executeSql($str);
	}
}
?>