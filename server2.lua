-- メインプログラムと一緒に動作する並列プログラムは、I/Oや変数などの設定に使用されます。モーションコマンドを呼び出すことはできません。
-- Version: Lua 5.3.5

Err, Socket = TCPCreate(true, "192.168.2.6", 6002)
TCPStart(Socket, 0)


while true do
  -- print(GetPose())
  p = GetPose()
  x =  p["coordinate"][1]
  y =  p["coordinate"][2]
  z =  p["coordinate"][3]
  r =  p["coordinate"][4]

  print(x)
  Err, RecBuf = TCPRead(Socket, 0, "string")
  TCPWrite(Socket, tostring(x)..","..tostring(y)..","..tostring(z)..","..tostring(r), 0)
end
