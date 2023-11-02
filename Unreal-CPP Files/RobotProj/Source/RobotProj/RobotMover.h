// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include <mongocxx/client.hpp>

#include "DatabaseConnection.h"
#include "RobotMover.generated.h"

UCLASS()
class ROBOTPROJ_API ARobotMover : public AActor
{
	GENERATED_BODY()
	
public:	
	// Sets default values for this actor's properties
	ARobotMover();

protected:
	// Called when the game starts or when spawned
	virtual void BeginPlay() override;

public:	
	// Called every frame
	virtual void Tick(float DeltaTime) override;

private:
	UPROPERTY(EditAnywhere, Category="Robot_Mover")
	FVector robotVelocity = FVector(10, 0, 0);
	UPROPERTY(EditAnywhere)
	FVector startLocation;

	UPROPERTY(VisibleAnywhere)
	double distance;
	UPROPERTY(EditAnywhere)
	double moveDistance;

	std::string className;
	std::string _id;

	UPROPERTY(VisibleAnywhere)
	double x;
	UPROPERTY(VisibleAnywhere)
	double z;
	
	UPROPERTY(EditAnywhere, Category = "DatabaseConnection")
	TSubclassOf<ADatabaseConnection> DatabaseClass;

	void MoveRobot(float DeltaTime);
	void getRobotInfo(std::optional<bsoncxx::document::value> cursor);
};
