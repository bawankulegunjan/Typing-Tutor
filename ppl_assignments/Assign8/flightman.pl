                                        /*Air Flight Management system */
/*Facts
flight(from,airline,to,price,duration)*/

flight(paris,united,toulouse,35,120).
flight(toulouse,united,paris,35,120).
flight(toronto,aircanada,london,500,360).
flight(london,aircanada,toronto,500,360).
flight(toronto,united,london,650,420).
flight(london,united,toronto,650,420).
flight(toronto,aircanada,madrid,900,480).
flight(madrid,aircanada,toronto,900,480).
flight(toronto,united,madrid,950,540).
flight(madrid,united,toronto,950,540).
flight(toronto,iberia,madrid,800,480).
flight(madrid,iberia,toronto,800,480).
flight(madrid,aircanada,barcelona,100,60).
flight(barcelona,aircanada,madrid,100,60).
flight(madrid,iberia,barcelona,120,65).
flight(barcelona,iberia,madrid,120,65).
flight(barcelona,iberia,london,220,240).
flight(london,iberia,barcelona,220,240).
flight(barcelona,iberia,valencia,110,75).
flight(valencia,iberia,barcelona,110,75).
flight(madrid,iberia,valencia,40,50).
flight(valencia,iberia,madrid,40,50).
flight(madrid,iberia,malaga,50,60).
flight(malaga,iberia,madrid,50,60).
flight(malaga,iberia,valencia,80,120).
flight(valencia,iberia,malaga,80,120).

/*airport(city,airporttax,minsecuritydelay)*/
airport(toronto,50,60).
airport(london,75,80).
airport(madrid,75,45).
airport(barcelona,40,30).
airport(valencia,40,20).
airport(malaga,50,30).
airport(paris,50,60).
airport(toulouse,40,30).

%Rules
/* is there a flight from toronto to madrid? */
pathflight(X,Z) :- flight(X,_,Z,_,_).
pathflight(X,Z) :- flight(X,_,Y,_,_) , pathflight(Y,Z).

/* A flight from city A to city B with airline C is cheap if its price is less than $400? */
checkcheap(A,C,B) :- flight(A,C,B,D,_),
		       D < 400.

/* is it possible to go from toronto to madrid */
twoflights(X,Y) :- flight(X,_,Z,_,_) , flight(Z,_,Y,_,_).

/*A flight from city A to city B with airline C is preferred if it's cheap(see(b)) or it's with with air_Canada ? */
prefered(A,C,B) :- checkcheap(A,C,B) ; C==aircanada.

/* if there is a flight from city A to city B with united , then there is a flight from city A to city B with air_Canada? */
flightsearch(A, B):-
	flight(A,united,B,_,_),
	write("Yes.. ! There is a flight with air-line United      "),
	flight(A,aircanada,B,_,_),
	write('Yes.. ! There is a flight with air-line Air_Canada').

displayflight() :- forall(flight(P,Q,R,S,T),(write(P),write("\t"),write(Q),write("\t"),write(R),write("\t"),write(S),write("\t"),writeln(T))).

displayairport() :- forall(airport(P,Q,R),(write(P),write("\t"),write(Q),write("\t"),writeln(R))).

