mkdir ./taxi
cd ./taxi

aws s3 cp s3://nyc-tlc/trip\ data/yellow_tripdata_2017-01.csv ./
aws s3 cp s3://nyc-tlc/trip\ data/yellow_tripdata_2017-02.csv ./
aws s3 cp s3://nyc-tlc/trip\ data/yellow_tripdata_2017-03.csv ./
aws s3 cp s3://nyc-tlc/trip\ data/yellow_tripdata_2017-04.csv ./
aws s3 cp s3://nyc-tlc/trip\ data/yellow_tripdata_2017-05.csv ./
aws s3 cp s3://nyc-tlc/trip\ data/yellow_tripdata_2017-06.csv ./


cat *.csv > yellow_tripdata_2017-1stHALF.csv