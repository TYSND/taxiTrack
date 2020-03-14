<?php
class mysqlHelper
{
	//链接数据库的变量
	private $con;
	//构造函数
	public function __construct()
    {
		$a = func_get_args(); //获取构造函数中的参数
        $i = count($a);
        if (method_exists($this,$f='__construct'.$i)) 
		{
			call_user_func_array(array($this,$f),$a);
        }
    }
	//0参数的构造函数
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
	//4参数的构造函数
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
	//执行SQL语句，并返回结果
	public function executeSql($sql)
	{
		return mysqli_query($this->con,$sql);
	}
	//改变数据库的默认提交状态,主要用于事务处理
	public function changeAutocommit($tf)
	{
		mysqli_autocommit($this->con,$tf);
	}
	//开启事务
	public function transaction()
	{
		mysqli_begin_transaction(MYSQLI_TRANS_START_READ_WRITE);
	}
	//手动提交SQL语句
	public function commit()
	{
		mysqli_commit($this->con);
	}
	//事务的回滚
	public function rollback()
	{
		mysqli_rollback($this->con);
	}
	//返回错误信息
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