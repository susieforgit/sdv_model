from sdv.model import Service

from my_vehicle_model.proto.seats_pb2 import (
    CurrentPositionRequest,
    MoveComponentRequest,
    MoveRequest,
    Seat,
    SeatComponent,
    SeatLocation,
)
from my_vehicle_model.proto.seats_pb2_grpc import SeatsStub


class SeatService(Service):
    "SeatService model"

    def __init__(self):
        super().__init__()
        self._stub = SeatsStub(self.channel)

    async def Move(self, seat: Seat):
        response = await self._stub.Move(MoveRequest(seat=seat), metadata=self.metadata)
        return response

    async def MoveComponent(
        self,
        seatLocation: SeatLocation,
        component: SeatComponent,
        position: int,
    ):
        response = await self._stub.MoveComponent(
            MoveComponentRequest(
                seat=seatLocation,
                component=component,  # type: ignore
                position=position,
            ),
            metadata=self.metadata,
        )
        return response

    async def CurrentPosition(self, row: int, index: int):
        response = await self._stub.CurrentPosition(
            CurrentPositionRequest(row=row, index=index),
            metadata=self.metadata,
        )
        return response