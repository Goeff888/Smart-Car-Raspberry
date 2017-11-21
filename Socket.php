<?php
#Code funktioniert und empfängt mehrere Dateien
set_time_limit(0);

// Turn on implicit output flushing so we see what we're getting as it comes in.
ob_implicit_flush();

// Set timeout in seconds
$timeout = 3;  

// Create a TCP/IP client socket.
$socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
if ($socket === false) {
    $result2 = "Error: socket_create() failed: reason: " .socket_strerror(socket_last_error()). "\n";
}

echo "Socket erzeugt";

// Server data

$host = '192.168.0.107';
$port = 9999;

$error = NULL;
$attempts = 0;
$timeout *= 1000;  // adjust because we sleeping in 1 millisecond increments
$connected = FALSE;
while (!($connected = socket_connect($socket, $host, $port)) && ($attempts++ < $timeout)) {
    echo "Verbindung hergestellt";
    $error = socket_last_error();
    if ($error != SOCKET_EINPROGRESS && $error != SOCKET_EALREADY) 
    {
        echo "Error Connecting Socket: ".socket_strerror($error) . "\n";
        socket_close($socket);
        return NULL;
    }
    usleep(1000);
}
        

if (!$connected) 
{
    echo "Error Connecting Socket: Connect Timed Out After " . $timeout/1000 . " seconds. ".socket_strerror(socket_last_error()) . "\n";
    socket_close($socket);
    return NULL;
}
// Write to the socket
$input="Hallo Hier ist der Text für den Server";
$input2 = $_POST["action"];
socket_write($socket, $input2, strlen ($input2)) or die("Could not write input\n");

echo "Send Enable back into socket to the Server";

// close the socket
socket_close($socket);

?>