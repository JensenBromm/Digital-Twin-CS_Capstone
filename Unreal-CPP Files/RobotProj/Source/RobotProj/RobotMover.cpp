// Fill out your copyright notice in the Description page of Project Settings.


#include "RobotMover.h"
#include <vector>

// Sets default values
ARobotMover::ARobotMover()
{
 	// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = true;

}

// Called when the game starts or when spawned
void ARobotMover::BeginPlay()
{
	Super::BeginPlay();

	startLocation = GetActorLocation();
}

// Called every frame
void ARobotMover::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);

	MoveRobot(DeltaTime);
}

void ARobotMover::MoveRobot(float DeltaTime)
{
	/* Move platform forward
	* - Get current location
	* - Add vector to that location
	* - Set the location */
	FVector currentLocat = GetActorLocation();
	currentLocat += robotVelocity * DeltaTime;
	SetActorLocation(currentLocat);

	distance = FVector::Dist(currentLocat, startLocation);
	if (distance > moveDistance)
	{
		FString name = GetName();
		float overshoot = distance - moveDistance;
		//UE_LOG(LogTemp, Warning, TEXT("%s Overshoot distance: %fcm"), *name, overshoot);

		FVector moveDirection = robotVelocity.GetSafeNormal();
		startLocation += moveDirection * moveDistance;
		SetActorLocation(startLocation);
		robotVelocity *= -1;
	}
}