console.log('bienvenue');

// class Raspberry
class Raspberry {
  constructor(id, gps) {
    this.id = id;
    this.gps = gps;
    this.volume = 10;
    this.music = null;
    this.state = 0;
  }

  //Method : getGPS
  //Goal   : obtain gps information
  getGPS(){
    return this.gps;
  }

  //Method : getId
  //Goal   : obtain id information
  getId(){
    return this.id;
  }

  //Method : volumeUp
  //Goal   : switch up the volume
  volumeUp(){
    if(this.volume < 20)
    {
      this.volume++;
      return 1;
    }
    return 0;
  }

  //Method : volumeDown
  //Goal   : switch own the volume
  volumeDown(){
    if(this.volume > 1)
    {
      this.volume--;
      return 1;
    }
    return 0;
  }


  //Method      : changeMusicTo
  //Goal        : Change the music
  //Parameter 1 : The music to play
  changeMusicTo(nameMusic){
    this.music = nameMusic
  }


  //Method : play
  //Goal   : switch music to play
  play(){
    this.state = 1;
  }

  
  //Method : pause
  //Goal   : switch music to pause
  pause(){
    this.state = 0;
  }

  serialize(){
    ob = { "id":this.id , "gps":this.gps , "volume":this.volume , "music":this.music , "state":this.state   };
    return ob;
  } 

}

var p = new Raspberry(3,3);
console.log(p.getGPS());
