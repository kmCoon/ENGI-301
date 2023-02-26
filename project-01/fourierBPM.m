

function fourierBPM


    [ye, Fs] = audioread("60_bpm.mp3");
    font = 14;
    %power = abs(fourier).^2/n;  
    m = length(ye);
    n = pow2(nextpow2(m));
    f = (0:n-1)*(Fs/n)/10;
    
    fourier = fft(ye,n);
    foyer = abs(fourier(1:floor(n/2)));
    fee = f(1:floor(n/2));
    
    hold on
    plot(fee,foyer)
    xlabel("Frequency (Hz)",'fontsize',font);
    ylabel("Power",'fontsize',font);
    [pks,indx] = findpeaks(foyer,'NPeaks',8,'MinPeakHeight',10);
    pks;
    bpm = round(mean(pks)*2) - 3
    plot(indx,pks,'.','markersize',10);
    
end



