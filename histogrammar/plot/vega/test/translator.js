var obj={
  "version": "1.0",
  "data": {
    "underflow:type": "Count",
    "overflow:type": "Count",
    "nanflow:type": "Count",
    "underflow": 0.0,
    "nanflow": 0.0,
    "values": [
      89.0,
      100.0,
      101.0,
      95.0,
      85.0,
      111.0,
      101.0,
      104.0,
      96.0,
      105.0,
      102.0,
      96.0,
      91.0,
      111.0,
      108.0,
      100.0,
      111.0,
      93.0,
      104.0,
      97.0
    ],
    "entries": 2000.0,
    "high": 1.0,
    "values:type": "Count",
    "overflow": 0.0,
    "low": 0.0
  },
  "type": "Bin"
};



for(var i=0;i<obj.length;i++){

    console.log(obj.data.values[i]);

}

