<?php

require '../DAO/mysqlHelper.php';
	$poi_file="../Data/beijingPOI.csv";
	$fpoi=fopen($poi_file,"r");
	fgetcsv($fpoi);//读掉表头
$mod=10000;
$cnt=0;
$mh=new mysqlHelper();
$mh->transaction();
$mh->changeAutocommit(FALSE);
	while($line_arr=fgetcsv($fpoi))
	{
		$cnt++;
		// if($cnt>10)
		// {
			// break;
		// }
		if($line_arr!='')
		{
			$poi=addslashes(iconv('GB2312','utf-8',$line_arr[0]));
			$cla=iconv('GB2312','utf-8',$line_arr[1]);
			$addr=addslashes(iconv('GB2312','utf-8',$line_arr[2]));
			$phone=addslashes(iconv('GB2312','utf-8',$line_arr[3]));
			$tel=addslashes(iconv('GB2312','utf-8',$line_arr[4]));
			$lon=iconv('GB2312','utf-8',$line_arr[5]);
			$lat=iconv('GB2312','utf-8',$line_arr[6]);
			
			$phone=explode(",",$phone);
			$phone=$phone[0];
			
			$tel=explode(",",$tel);
			$tel=$phone[0];
			
			//echo $poi.",".$addr.",".$phone.",".$tel.",".$lon.",".$lat.PHP_EOL;
			
			$sql="insert into poi_info 
				(poi_name,poi_addr,phone,tel,lon,lat)
				values
				('{$poi}','{$addr}','{$phone}','{$tel}',$lon,$lat)
				";
			$res=$mh->executeSql($sql);
			echo $mh->error().PHP_EOL;
			if($res==false)
			{
				//break;
			}
			if($cnt%$mod==0)
			{
				$mh->commit();
				sleep(1);
			}
			echo $cnt.PHP_EOL;
			/*
			//处理分类
			//$cla=substr($cla,1,strlen($cla)-2);
			$rplc=array('[',']');
			$cla=str_replace($rplc,'',$cla);
			$cla_arr=explode(",",$cla);
			print_r($cla_arr);
			echo PHP_EOL;
			*/
			
			
		}
	}
$mh->commit();
$mh->changeAutocommit(TRUE);
	fclose($fpoi);
	

?>