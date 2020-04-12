<?php
	$poi_file="../Data/beijingPOI.csv";
	$fpoi=fopen($poi_file,"r");
	$i=0;
	while($line_arr=fgetcsv($fpoi))
	{
		$i++;
		if($i==1)
		{
			continue;
		}
		if($i>10)
		{
			break;
		}
		if($line_arr!='')
		{
			foreach($line_arr as $col)
			{
				//echo gettype($col)." ";
				$pos=iconv('GB2312','utf-8',$col);   
				echo $pos." ";
				
			}
			//$pos=iconv('GB2312','utf-8',$line_arr[0]);   
			//$str=implode(",",$line_arr);
			//$encode = mb_detect_encoding($str, array("ASCII",'UTF-8',"GB2312","GBK",'BIG5')); 
			//echo $encode.PHP_EOL;
			//$pos = mb_convert_encoding($line_arr[0],'utf-8','GB2312');
			//print_r($str);
			//echo $pos;
			echo PHP_EOL;
		}
	}
	fclose($fpoi);
	

?>