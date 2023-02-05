for i = 1:1:10
    data = pyrunfile("aim.py", "data");
    pause(1);
    pyrunfile("aim.py");
end
