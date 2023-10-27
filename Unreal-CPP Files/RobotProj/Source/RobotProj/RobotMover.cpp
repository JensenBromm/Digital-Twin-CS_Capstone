// Fill out your copyright notice in the Description page of Project Settings.


#include "RobotMover.h"

#include "Public/DatabaseConnection.h"
THIRD_PARTY_INCLUDES_START
#include <vector>
#include <cstdlib>
#include <memory>
#include <mongocxx/database.hpp>
#include <bsoncxx/builder/basic/array.hpp>
#include <bsoncxx/builder/basic/document.hpp>
#include <bsoncxx/builder/basic/kvp.hpp>
#include <bsoncxx/json.hpp>
THIRD_PARTY_INCLUDES_END

using bsoncxx::builder::basic::kvp;
using bsoncxx::builder::basic::make_array;
using bsoncxx::builder::basic::make_document;
using bsoncxx::stdx::string_view;

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
	name = GetActorLabel();
}

// Called every frame
void ARobotMover::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);

	MoveRobot(DeltaTime);
	if (DatabaseClass)
	{
		std::string robotName = std::string(TCHAR_TO_UTF8(*name));
		//TODO Pass in collection instead of cursor
		double x = getRobotInfo(DatabaseClass->GetDefaultObject<ADatabaseConnection>()->getXCoord(robotName));
	}
	
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
		float overshoot = distance - moveDistance;
		//UE_LOG(LogTemp, Warning, TEXT("%s Overshoot distance: %fcm"), *name, overshoot);

		FVector moveDirection = robotVelocity.GetSafeNormal();
		startLocation += moveDirection * moveDistance;
		SetActorLocation(startLocation);
		robotVelocity *= -1;
	}
}

double ARobotMover::getRobotInfo(std::optional<bsoncxx::document::value> cursor)
{
	auto x = cursor.value().view()["x"];
	double xCoord = bsoncxx::types::b_double(x.get_double().value);
	UE_LOG(LogTemp, Log, TEXT("%s X coord = %f"), *FString(name), xCoord);
	return xCoord;
}