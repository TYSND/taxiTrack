<?php
require '../DAO/mysqlHelper.php';
function getLines($file) {
	$f = fopen($file, 'r');
	try {
		while ($line = fgets($f)) {
			yield $line;
		}
	} finally {
		fclose($f);
	}
}

$res=getLines('oneday.txt');
$tenmil=100000;
$cnt=1;
$mh=new mysqlHelper();
$mh->transaction();
$mh->changeAutocommit(FALSE);
foreach ($res as $n => $line) {
	if(strlen($line)==2)	break;
	echo $cnt;
	echo "\n";
	$info=explode(',',$line);
	$taxi_id=$info[0];
	$full_load=$info[1];
	$actual_load=$info[2];
	$info_date=$info[3];
	$lon=$info[4];
	$lat=$info[5];
	$attr1=$info[6];
	$attr2=$info[7];
	$attr3=$info[8];
	$sql="insert into taxi_info 
		(taxi_id,full_load,actual_load,info_date,lon,lat,attr1,attr2,attr3)
		values
		('{$taxi_id}',$full_load,$actual_load,'{$info_date}',$lon,$lat,$attr1,$attr2,$attr3)
		";
	$res=$mh->executeSql($sql);
	$cnt++;
	if($cnt%$tenmil==0)
	{
		$mh->commit();
	}
}
$mh->commit();
$mh->changeAutocommit(TRUE);
?>