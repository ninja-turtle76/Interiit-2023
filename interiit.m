for i = 1:1:10
    data = pyrunfile("infer.py", "data");
    if data.length > 0
        xc = double(data(1));
        yc = double(data(2));
        nw = double(data(3));
        nh = double(data(4));
        ax = "";
        ay = "";
        if xc>0.55
            ax = "Right";
        end
        if xc<0.45
            ax = "Left";
        end
        if yc>0.55
            ay = "Up";
        end
        if yc>0.45
            ay = "Down";
        end
    end
    pause(1);
end
