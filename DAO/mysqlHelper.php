<?php
class mysqlHelper
{
	private $con;
	public function __construct()
    {
		$a = func_get_args(); //获取构造函数中的参数
        $i = count($a);
        if (method_exists($this,$f='__construct'.$i)) 
		{
			call_user_func_array(array($this,$f),$a);
        }
    }
    function __construct0()
    {
        $this->con = mysqli_connect("localhost","root","a46513");
		if (!$this->con)
		{
			die('Could not connect: ' . mysqli_error());
		}
		mysqli_select_db($this->con,"taxitrack");
		mysqli_set_charset($this->con,"utf8");
    }
	function __construct4($host,$user,$pw,$db)
    {
		$this->con = mysqli_connect($host,$user,$pw);
		if (!$this->con)
		{
			die('Could not connect: ' . mysqli_error());
		}
		mysqli_select_db($this->con,$db);
		mysqli_set_charset($this->con,"utf8");
    }
	
	public function executeSql($sql)
	{
		return mysqli_query($this->con,$sql);
	}
	
	public function changeAutocommit($tf)
	{
		mysqli_autocommit($this->con,$tf);
	}
	public function transaction()
	{
		mysqli_begin_transaction(MYSQLI_TRANS_START_READ_WRITE);
	}
	public function commit()
	{
		mysqli_commit($this->con);
	}
	public function rollback()
	{
		mysqli_rollback($this->con);
	}
	public function error()
	{
		return mysqli_error($this->con);
	}
}

/*
$mh0=new mysqlHelper();
//$mh0->select();
$mh4=new mysqlHelper('localhost','root','a46513','taxitrack');
*/

?>